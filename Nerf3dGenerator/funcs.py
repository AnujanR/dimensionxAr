import os
import subprocess

def extract_frames_from_video(video_path, output_dir):

    colmap2nerf_path =os.path.join(os.getcwd(), 'Nerf3dGenerator/libraries/instant_ngp/scripts/', 'colmap2nerf.py')

    # Define the command to extract images from the video using colmap2nerf.py
    command = ['python', colmap2nerf_path, '--video_in', output_dir+video_path, '--video_fps', '4', '--run_colmap', '--aabb_scale','4', '--out', output_dir + 'transforms.json']

    # Execute the command
    result = subprocess.run(command, capture_output=True)

    # Check if the command was successful
    if result.returncode == 0:
        print('Video frames extracted successfully.')
    else:
        print('Error: ', result.stderr.decode('utf-8'))


def train_scene_model(video_path, scene_path):

    run_path =os.path.join(os.getcwd(), 'Nerf3dGenerator/libraries/instant_ngp/scripts/', 'run.py')
    train_steps=2500

    # Define the command to train images from the video using run.py
    command = ['python', run_path, scene_path, ' --n_steps ', f'{train_steps}', '--save_snapshot ',os.path.join(scene_path, f"{train_steps}.ingp"),'--save_mesh',os.path.join(scene_path, f"{train_steps}.obj")]

    # Execute the command
    result = subprocess.run(command, capture_output=True)

    # Check if the command was successful
    if result.returncode == 0:
        print('Scene Trained successfully.')
    else:
        print('Error: ', result.stderr.decode('utf-8'))