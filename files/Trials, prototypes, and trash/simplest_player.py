import pygame
import os

def music_player(file_path):
    """Music player with basic controls"""
    pygame.init()
    pygame.mixer.init()
    
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Playing: {os.path.basename(file_path)}")
        print("Commands: p=pause, r=resume, s=stop, q=quit")
        
        while True:
            cmd = input("Enter command: ").lower()
            
            if cmd == 'p':
                pygame.mixer.music.pause()
            elif cmd == 'r':
                pygame.mixer.music.unpause()
            elif cmd == 's':
                pygame.mixer.music.stop()
                break
            elif cmd == 'q':
                break
                
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pygame.mixer.quit()
        pygame.quit()

# Example usage
if __name__ == "__main__":
    music_file = "Songs\\mp3\\Car Seat Headrest - Culture.mp3"
    
    if os.path.exists(music_file):
        music_player(music_file)
    else:
        print("Music file not found!")
