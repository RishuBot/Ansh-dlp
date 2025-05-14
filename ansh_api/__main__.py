import sys
import subprocess

def main():
    if len(sys.argv) < 2:
        print("ansh-api - Powered by Ansh")
        print("Usage: ansh-api <youtube_url or options>")
        sys.exit(1)

    cmd = ['yt-dlp'] + sys.argv[1:]
    subprocess.run(cmd)

if __name__ == '__main__':
    main()
