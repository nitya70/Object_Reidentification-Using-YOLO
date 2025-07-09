import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def detect_team(crop):
    if crop is None or crop.size == 0:
        return "?"

    hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)

    red1 = cv2.inRange(hsv, (0, 50, 50), (10, 255, 255))
    red2 = cv2.inRange(hsv, (160, 50, 50), (180, 255, 255))
    red_mask = red1 | red2

    white_mask = cv2.inRange(hsv, (0, 0, 200), (180, 40, 255))
    yellow_mask = cv2.inRange(hsv, (20, 100, 100), (35, 255, 255))

    red_pct = np.sum(red_mask > 0) / crop.size
    white_pct = np.sum(white_mask > 0) / crop.size
    yellow_pct = np.sum(yellow_mask > 0) / crop.size

    if red_pct > 0.01:
        return "R"
    elif white_pct > 0.01:
        return "W"
    elif yellow_pct > 0.01:
        return "Y"
    return "?"

def team_color(team, for_cv=False):
    team = team.strip().upper()
    color_hex = {
        "R": "#ff4c4c",    # Red team
        "W": "#4c8cff",    # Blue/white team
        "Y": "#f8e71c",    # Referee
        "?": "#888888"
    }.get(team, "#888888")

    if not for_cv:
        return color_hex

    # Convert HEX to BGR for OpenCV
    h = color_hex.lstrip("#")
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return (rgb[2], rgb[1], rgb[0])

def setup_tactical_map(frame_shape):
    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, frame_shape[1])
    ax.set_ylim(frame_shape[0], 0)
    ax.axis('off')
    return fig, ax

def update_tactical_map(ax, positions):
    ax.clear()
    ax.set_xlim(0, 1280)
    ax.set_ylim(720, 0)
    ax.axis('off')
    ax.set_title("Tactical Map - Live")

    for cx, cy, label, color in positions:
        dot = patches.RegularPolygon((cx, cy), numVertices=4, radius=7, orientation=np.pi / 4, color=color)
        ax.add_patch(dot)
        ax.text(cx, cy - 12, label, ha='center', va='bottom', fontsize=8, color='black', weight='bold')

    plt.pause(0.001)

class GlobalTracker:
    def __init__(self, dist_thresh=60): 
        self.players = {}
        self.next_id = 0
        self.dist_thresh = dist_thresh

    def _euclidean(self, a, b):
        return np.linalg.norm(np.array(a) - np.array(b))

    def match_or_create(self, det_center, team):
        best_gid = None
        best_dist = float("inf")

        for gid, info in self.players.items():
            if info["team"] != team:
                continue
            dist = self._euclidean(det_center, info["last_pos"])
            if dist < self.dist_thresh and dist < best_dist:
                best_dist = dist
                best_gid = gid

        if best_gid is not None:
            self.players[best_gid]["last_pos"] = det_center
        else:
            best_gid = self.next_id
            self.players[best_gid] = {"team": team, "last_pos": det_center}
            self.next_id += 1

        return best_gid
