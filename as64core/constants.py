DEFAULT_FRAME_RATE = 29.97
DEFAULT_LS_HOST = "localhost"
DEFAULT_LS_PORT = 16834

GAME_JP = "JP"
GAME_US = "US"

PREDICTION_MODE = 0
CONFIRMATION_MODE = 1

TIMING_RTA = "RTA"
TIMING_UP_RTA = "Up RTA"
TIMING_FILE_SELECT = "File Select"

SPLIT_NORMAL = "Normal"
SPLIT_FADE_ONLY = "Fade"
SPLIT_FINAL = "Final"
SPLIT_MIPS = "Mips"
SPLIT_MIPS_X = "Mips-X"
SPLIT_XCAM = "X-Cam"
SPLIT_INITIAL = "Initial"

NO_FADE = "NO_FADE"
FADEOUT_PARTIAL = "FADEOUT_PARTIAL"
FADEOUT_COMPLETE = "FADEOUT_COMPLETE"
FADEIN_PARTIAL = "FADEIN_PARTIAL"
FADEIN_COMPLETE = "FADEIN_COMPLETE"

GAME_REGION = 0
STAR_REGION = 1
LIFE_REGION = 2
FADEOUT_REGION = 3
FADEIN_REGION = 4
RESET_REGION = 5
NO_HUD_REGION = 6
POWER_REGION = 7
XCAM_REGION = 8

GAME_REGION_BASE = [617, 454]
GAME_REGION_RATIO = [0, 0, 617, 454]
STAR_REGION_US_RATIO = [513, 7, 89, 47]
STAR_REGION_JP_RATIO = [521, 6, 89, 47]
LIFE_REGION_US_RATIO = [36, 13, 63, 442]
LIFE_REGION_JP_RATIO = [36, 10, 63, 42]
FADEOUT_REGION_RATIO = [283, 206, 50, 50]
FADEIN_REGION_RATIO = [230, 90, 157, 50]
RESET_REGION_RATIO = [190, 137, 251, 137]
NO_HUD_REGION_RATIO = [0, 106, 617, 285]
POWER_REGION_RATIO = [246, 48, 52, 46]

XCAM_REGION_RATIO = [555, 403, 23, 23]

MODEL_PATH = "resources/model/star_predictor.onnx"
MODEL_PATH_LEGACY = "resources/model/default_model.onnx"
MODEL_WIDTH = 67
MODEL_HEIGHT = 40
