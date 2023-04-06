from PIL import Image
import torch
from tqdm.auto import tqdm
import argparse
import trimesh
from point_e.diffusion.configs import DIFFUSION_CONFIGS, diffusion_from_config
from point_e.diffusion.sampler import PointCloudSampler
from point_e.models.download import load_checkpoint
from point_e.models.configs import MODEL_CONFIGS, model_from_config
from point_e.util.plotting import plot_point_cloud
from point_e.util.pc_to_mesh import marching_cubes_mesh

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='point cloud generator')

    # Define the arguments
    parser.add_argument('--imgpath', type=str, help='image path define')
    parser.add_argument('--out', type=str,  help='out path define')

    # Parse the arguments
    args = parser.parse_args()

    # Access the parsed arguments
    imgpath = args.imgpath
    outpath = args.out

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print('creating base model...')
    base_name = 'base40M'  # use base300M or base1B for better results
    base_model = model_from_config(MODEL_CONFIGS[base_name], device)
    base_model.eval()
    base_diffusion = diffusion_from_config(DIFFUSION_CONFIGS[base_name])

    print('creating upsample model...')
    upsampler_model = model_from_config(MODEL_CONFIGS['upsample'], device)
    upsampler_model.eval()
    upsampler_diffusion = diffusion_from_config(DIFFUSION_CONFIGS['upsample'])

    print('downloading base checkpoint...')
    base_model.load_state_dict(load_checkpoint(base_name, device))

    print('downloading upsampler checkpoint...')
    upsampler_model.load_state_dict(load_checkpoint('upsample', device))

    sampler = PointCloudSampler(
    device=device,
    models=[base_model, upsampler_model],
    diffusions=[base_diffusion, upsampler_diffusion],
    num_points=[1024, 4096 - 1024],
    aux_channels=['R', 'G', 'B'],
    guidance_scale=[3.0, 3.0],
    )

    img = Image.open(imgpath)
    samples = None
    for x in tqdm(sampler.sample_batch_progressive(batch_size=1, model_kwargs=dict(images=[img]))):
        samples = x

    pc = sampler.output_to_point_clouds(samples)[0]


    name = 'sdf'
    model = model_from_config(MODEL_CONFIGS[name], device)
    model.eval()
    model.load_state_dict(load_checkpoint(name, device))

    mesh = marching_cubes_mesh(
        pc=pc,
        model=model,
        batch_size=4096,
        grid_size=32,  # increase to 128 for resolution used in evals
        progress=True,
    )

    with open(outpath, 'wb') as f:
        mesh.write_ply(f)
