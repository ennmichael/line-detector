# line-detector

This is a small Python program used to detect weather certain hand-drawn strokes approximate lines.
It does this by splitting the stroke into a fixed number of parts,
and checking the growth rate (angle) of each part. The detection logic is in `detection.py`.

### Running
On Windows:
```
cd <project repository>
.\venv\Scripts\python.exe main.py
```

On Unix:
```
cd <project repository>
source bin/activate
python main.py
```

### Demo

!["Demo gif"](/demo.gif)