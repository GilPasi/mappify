import math
import numpy as np 

def get_stripe_range(stripe: np.ndarray):
    start = end = 0 

    for i in range(len(stripe)): 
        if start == 0 and stripe[i] > 0: 
            start = i
        if end == 0 and stripe[-i] > 0:
            end = len(stripe) - i
        if end != 0 and start != 0:
            break 
    return start, end

def get_stripe_width(stripe: np.ndarray):
    start, end = get_stripe_range(stripe)
    return end - start

def get_average_depth(stripe: np.ndarray):
    start, end =  get_stripe_range(stripe)
    return sum(stripe[start:end+1]) / (end - start + 1)


def calculate_real_life_width(pixels: np.ndarray, focal_length: float, sensor_width: float):
    non_zero_indices = np.where(pixels > 0)[0]

    if non_zero_indices.size == 0:
        return 0

    depths = pixels[non_zero_indices]
    MEAN_POWER = 1.75
    avg_powered_depth = (np.mean(depths))**MEAN_POWER
    fov = 2 * np.arctan(sensor_width / (2 * focal_length))
    pixel_width = non_zero_indices[-1] - non_zero_indices[0] + 1
    width_at_avg_depth = 2 * avg_powered_depth * np.tan(fov / 2)
    real_life_width = width_at_avg_depth * (pixel_width / len(pixels))

    return real_life_width

def multiple_normalize_object_width(images: list):
    return [normalize_object_width(img) for img in images]


def normalize_object_width(image: np.ndarray):
    # TODO: Get FOCAL_WIDTH from react native and SENSOR_WIDTH from database ( and react tn).
    SENSOR_WIDTH = 11.95
    FOCAL_WIDTH = 26



    middle_stripe_idx = len(image) // 2

    real_width_base_stripe = calculate_real_life_width(
        image[middle_stripe_idx], FOCAL_WIDTH, SENSOR_WIDTH)
    pixel_width_base_stripe = calculate_stripe_pixels(image[middle_stripe_idx])
    
    SQUEEZE_FACTOR = 2.5
    for idx, stripe in enumerate(image): 
        real_width_current_stripe = calculate_real_life_width(
            stripe, FOCAL_WIDTH, SENSOR_WIDTH)
        # Avoid blank lines bugs
        if real_width_current_stripe == 0: 
            continue 

        real_width_base_stripe = max(real_width_base_stripe, 1 ) # Avoid divison by zero 
        real_ratio = real_width_current_stripe / (real_width_base_stripe * SQUEEZE_FACTOR)
        real_ratio **= 2
        new_current_stripe_width = int(pixel_width_base_stripe * real_ratio)
        new_stripe = normalize_stripe(stripe, new_current_stripe_width)
        image[idx, :] = new_stripe
        
    return image


def normalize_stripe(stripe: np.ndarray, new_width: int):
    stripe_middle = calculate_middle_point(stripe)
    new_width = min(new_width, stripe.shape[0]) // 2 # Avoid Out of bound
    LIGHT_VAL = 255
    new_stripe = np.zeros(len(stripe))

    for i in range(new_width):
        if stripe_middle + i < len(new_stripe):
            new_stripe[stripe_middle + i] = LIGHT_VAL

        if stripe_middle - i >= 0:
            new_stripe[stripe_middle - i] = LIGHT_VAL
    return new_stripe

def calculate_middle_point(stripe: np.ndarray):
    start, end = get_stripe_range(stripe)
    return start + calculate_stripe_pixels(stripe) // 2

    
def calculate_stripe_pixels(stripe: np.ndarray):
    start, end = get_stripe_range(stripe)
    return int(end - start)
        
    
    
        
