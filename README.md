# KCD Istanbul 2024 Website

## Development

### Install dependencies

- Install Hugo: https://gohugo.io/installation/

### Run the website locally

```bash
make serve
```

Open http://localhost:1313/ in your browser.

### Build the website

```bash
make build
```

The website will be built in the `public` directory.

### Optimizing images

We do image optimization (making them smaller, making them Web compatible, etc.) using imagemagick. You can install it using `brew install imagemagick` on macOS.

To optimize images, run the following command:

```bash
# Optimize all images in the speakers directory
# max speaker image size should be 600x600 (\> means only shrink larger images)
# strip exif data
# set quality to 80
mogrify -resize 600x600\> -strip -quality 80 static/speakers/*.jpg
mogrify -resize 600x600\> -strip -quality 80 static/speakers/*.png
mogrify -resize 600x600\> -strip -quality 80 static/speakers/*.jpeg
mogrify -resize 600x600\> -strip -quality 80 static/speakers/*.webp

# same story for team directory
mogrify -resize 600x600\> -strip -quality 80 static/team/*.jpg
mogrify -resize 600x600\> -strip -quality 80 static/team/*.png
mogrify -resize 600x600\> -strip -quality 80 static/team/*.jpeg
mogrify -resize 600x600\> -strip -quality 80 static/team/*.webp
```

To re-compress PNG images, we use `pngquant`. You can install it using `brew install pngquant` on macOS.

```bash
# Optimize all PNG images in the speakers directory
pngquant --force --ext .png static/speakers/*.png
# Same story for team directory
pngquant --force --ext .png static/team/*.png
# Same story for sponsors directory
pngquant --force --ext .png static/sponsors/*.png
```


## Publishing

The website is hosted on Netlify. Pushing to the `main` branch will trigger a
new build and deploy.

## Favicon

Favicons are generated by https://cthedot.de/icongen/
