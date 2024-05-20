randomize_photos:
	echo "Randomizing photos..."
	python3 assets/photos/randomize.py

build: randomize_photos
	echo "Building the site..."
	hugo
