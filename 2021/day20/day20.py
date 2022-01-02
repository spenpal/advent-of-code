def print_image(image):
    for row in image:
        for pixel in row:
            print(pixel, end='')
        print()

def trim_image(image, remove_padding):
    image = image[remove_padding:]
    image = image[:-remove_padding]
    image = [row[remove_padding: -remove_padding] for row in image]
    return image

def pixel_enhancement(image, row_idx, col_idx, algorithm):
    nine_pixels = []
    nine_pixels.append(image[row_idx - 1][col_idx - 1: col_idx + 2])
    nine_pixels.append(image[row_idx][col_idx - 1: col_idx + 2])
    nine_pixels.append(image[row_idx + 1][col_idx - 1: col_idx + 2])
    nine_pixels = ''.join(nine_pixels)
    
    binary_num = ''.join('1' if pixel == '#' else '0' for pixel in nine_pixels)
    output_pixel_idx = int(binary_num, 2)
    
    return algorithm[output_pixel_idx]

def image_enhancement(input_image, algorithm):
    output_image = ['.' * len(input_image[0]) for _ in range(len(input_image))]
    
    start = 1
    for row_idx in range(start, len(output_image) - start):
        new_pixel_row = []
        for col_idx in range(start, len(output_image) - start):
            output_pixel = pixel_enhancement(input_image, row_idx, col_idx, algorithm)
            new_pixel_row.append(output_pixel)
        output_image[row_idx] = ('.' * start) + ''.join(new_pixel_row) + ('.' * start)
    
    return output_image

def add_image_padding(image, padding):
    top_padding = ['.' * (len(image[0]) + padding * 2) for _ in range(padding)]
    side_padding = [''.join(['.' * padding, row, '.' * padding]) for row in image]
    bottom_padding = ['.' * (len(image[0]) + padding * 2) for _ in range(padding)]
    return top_padding + side_padding + bottom_padding
   
def enhance(input_image, algorithm, steps):
    padding = len(input_image)
    input_image = add_image_padding(input_image, padding)
    
    for _ in range(steps):
        input_image = image_enhancement(input_image, algorithm)
        
    output_image = input_image
    remove_padding = padding - steps
    output_image = trim_image(output_image, remove_padding)
    return sum(1 for row in output_image for pixel in row if pixel == '#')

def main():
    with open("puzzle_input.txt") as f:
        algorithm = f.readline().strip()
        f.readline()
        input_image = f.read().splitlines()
        
    print(f"Part 1 Answer: {enhance(input_image, algorithm, 2)}")
    print(f"Part 2 Answer: {enhance(input_image, algorithm, 50)}")

if __name__ == "__main__":
    main()