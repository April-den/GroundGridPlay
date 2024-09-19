"""
Continuously visualize frames
"""
import sys, os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..' ))
sys.path.append(BASE_DIR)

import numpy as np
from pathlib import Path
from tqdm import tqdm
import open3d as o3d
import fire, time
from utils.o3d_view import MyVisualizer


class SegmentedCloud:
    def __init__(self, directory):
        super(SegmentedCloud, self).__init__()
        self.scene_id = directory.split("/")[-1]
        self.directory = Path(directory) / "pcd"
        self.pcd_files = [os.path.join(self.directory, f) for f in sorted(os.listdir(self.directory)) if
                          f.endswith('.txt')]
        print(self.pcd_files[9])


    def __len__(self):
        return len(self.pcd_files)

    def __getitem__(self, index_):
        res_dict = {
            'scene_id': self.scene_id,
        }
        data = np.loadtxt(self.pcd_files[index_])
        points = data[:, :3]
        labels = data[:, 3].astype(int)
        point_cloud = o3d.geometry.PointCloud()
        point_cloud.points = o3d.utility.Vector3dVector(points)
        colors = np.zeros((points.shape[0], 3))
        colors[labels == 49] = [0, 1, 0]
        colors[labels == 99] = [1, 0, 0]
        point_cloud.colors = o3d.utility.Vector3dVector(colors)
        res_dict['pc'] = point_cloud

        return res_dict


def vis(
        data_dir: str = "/home/aiyang/groundgrid",
        view_file: str = os.path.abspath(BASE_DIR + "/pythonProject/default.json"),
        point_size: int = 3,
        speed: int = 1,
):
    o3d_vis = MyVisualizer(view_file=view_file, window_title="GroundGrid View")
    opt = o3d_vis.vis.get_render_option()
    opt.point_size = point_size

    dataset = SegmentedCloud(data_dir)

    # vis = o3d.visualization.Visualizer()
    # vis.create_window()
    # vis.add_geometry(dataset[2]['pc'])

    for data_id in (pbar := tqdm(range(0, len(dataset)))):
        data = dataset[data_id]
        o3d_vis.update([data['pc'], o3d.geometry.TriangleMesh.create_coordinate_frame(size=1)])
        # vis.update_geometry(data['pc'])
        # vis.poll_events()
        # vis.update_renderer()

        # o3d.visualization.draw_geometries([pcd])
        # o3d_vis.update([pcd, o3d.geometry.TriangleMesh.create_coordinate_frame(size=1)])
        time.sleep(0.05 * 1 / speed)


if __name__ == "__main__":
    fire.Fire(vis)
    pass