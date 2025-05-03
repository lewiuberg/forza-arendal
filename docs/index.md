---
author: "Lewi Lie Uberg"
hide:
  - navigation
  - toc
  - feedback
---

# Velkommen til Forza Arendal

Forza Arendal er supporter klubben for Arendal Fotball. Her finner du informasjon om klubben, supporterklubben og hvordan du kan bli med i fellesskapet vårt.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

<!-- <div style="text-align: center;"><iframe width="80%" height="200" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/2087557665&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true\"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/lewiuberg\" title="lewiuberg" target="_blank" style="color: #cccccc; text-decoration: none;">lewiuberg</a> · <a href="https://soundcloud.com/lewiuberg/forza-arendal\" title="Forza-Arendal" target="_blank" style="color: #cccccc; text-decoration: none;">Forza-Arendal</a></div></div> -->

<script>
  let currentIndex = 0;

  // List of prioritized images (GIFs first)
  const prioritizedImages = [
    "./assets/images/arkiv/500.gif",
    "./assets/images/arkiv/501.gif",
    "./assets/images/arkiv/1.jpg",
    "./assets/images/arkiv/8.jpg",
    "./assets/images/arkiv/11.jpg",
    "./assets/images/arkiv/13.jpg",
    "./assets/images/arkiv/16.jpg",
    "./assets/images/arkiv/20.jpg",
    "./assets/images/arkiv/14.jpg",
  ];

  // Full list of images
  const allImages = [
    "./assets/images/arkiv/500.gif",
    "./assets/images/arkiv/501.gif",
    "./assets/images/arkiv/1.jpg",
    "./assets/images/arkiv/2.jpg",
    "./assets/images/arkiv/3.jpg",
    "./assets/images/arkiv/4.jpg",
    "./assets/images/arkiv/5.jpg",
    "./assets/images/arkiv/6.jpg",
    "./assets/images/arkiv/7.jpg",
    "./assets/images/arkiv/8.jpg",
    "./assets/images/arkiv/9.jpg",
    "./assets/images/arkiv/10.jpg",
    "./assets/images/arkiv/11.jpg",
    "./assets/images/arkiv/12.jpg",
    "./assets/images/arkiv/13.jpg",
    "./assets/images/arkiv/14.jpg",
    "./assets/images/arkiv/15.jpg",
    "./assets/images/arkiv/16.jpg",
    "./assets/images/arkiv/17.jpg",
    "./assets/images/arkiv/18.jpg",
    "./assets/images/arkiv/19.jpg",
    "./assets/images/arkiv/20.jpg",
    "./assets/images/arkiv/21.jpg",
    "./assets/images/arkiv/22.jpg",
    "./assets/images/arkiv/23.jpg",
    "./assets/images/arkiv/24.jpg",
    "./assets/images/arkiv/25.jpg",
    "./assets/images/arkiv/26.jpg",
    "./assets/images/arkiv/27.jpg",
    "./assets/images/arkiv/28.jpg",
    "./assets/images/arkiv/29.jpg",
    "./assets/images/arkiv/30.jpg",
    "./assets/images/arkiv/31.jpg",
    "./assets/images/arkiv/32.jpg",
    "./assets/images/arkiv/33.jpg",
    "./assets/images/arkiv/34.jpg",
    "./assets/images/arkiv/35.jpg",
    "./assets/images/arkiv/36.jpg",
    "./assets/images/arkiv/37.jpg",
    "./assets/images/arkiv/38.jpg",
    "./assets/images/arkiv/39.jpg",
    "./assets/images/arkiv/40.jpg",
    "./assets/images/arkiv/41.jpg",
    "./assets/images/arkiv/42.jpg",
    "./assets/images/arkiv/43.jpg",
    "./assets/images/arkiv/44.jpg",
    "./assets/images/arkiv/45.jpg",
    "./assets/images/arkiv/46.jpg",
    "./assets/images/arkiv/47.jpg",
    "./assets/images/arkiv/48.jpg",
    "./assets/images/arkiv/49.jpg",
    "./assets/images/arkiv/50.jpg",
    "./assets/images/arkiv/51.jpg",
    "./assets/images/arkiv/52.jpg",
    "./assets/images/arkiv/53.jpg",
    "./assets/images/arkiv/54.jpg",
    "./assets/images/arkiv/55.jpg",
    "./assets/images/arkiv/56.jpg",
    "./assets/images/arkiv/57.jpg",
    "./assets/images/arkiv/58.jpg",
    "./assets/images/arkiv/59.jpg",
    "./assets/images/arkiv/60.jpg",
    "./assets/images/arkiv/61.jpg",
    "./assets/images/arkiv/62.jpg",
    "./assets/images/arkiv/63.jpg",
    "./assets/images/arkiv/64.jpg",
    "./assets/images/arkiv/65.jpg",
    "./assets/images/arkiv/66.jpg",
    "./assets/images/arkiv/67.jpg",
    "./assets/images/arkiv/68.jpg",
    "./assets/images/arkiv/69.jpg",
    "./assets/images/arkiv/70.jpg",
    "./assets/images/arkiv/71.jpg",
    "./assets/images/arkiv/72.jpg",
    "./assets/images/arkiv/73.jpg",
    "./assets/images/arkiv/74.jpg",
    "./assets/images/arkiv/75.jpg",
    "./assets/images/arkiv/76.jpg",
    "./assets/images/arkiv/77.jpg",
    "./assets/images/arkiv/78.jpg",
    "./assets/images/arkiv/79.jpg",
    "./assets/images/arkiv/80.jpg",
    "./assets/images/arkiv/81.jpg",
    "./assets/images/arkiv/82.jpg",
    "./assets/images/arkiv/83.jpg",
    "./assets/images/arkiv/84.jpg",
    "./assets/images/arkiv/85.jpg",
    "./assets/images/arkiv/86.jpg",
    "./assets/images/arkiv/87.jpg",
    "./assets/images/arkiv/88.jpg",
    "./assets/images/arkiv/89.jpg",
    "./assets/images/arkiv/90.jpg",
    "./assets/images/arkiv/91.jpg",
    "./assets/images/arkiv/92.jpg",
    "./assets/images/arkiv/93.jpg",
    "./assets/images/arkiv/94.jpg",
    "./assets/images/arkiv/95.jpg",
    "./assets/images/arkiv/96.jpg",
    "./assets/images/arkiv/97.jpg",
    "./assets/images/arkiv/98.jpg",
    "./assets/images/arkiv/99.jpg",
    "./assets/images/arkiv/100.jpg",
    "./assets/images/arkiv/101.jpg",
    "./assets/images/arkiv/102.jpg",
    "./assets/images/arkiv/103.jpg",
    "./assets/images/arkiv/104.jpg",
    "./assets/images/arkiv/105.jpg",
    // Add more image paths as needed
  ];

  // Combine prioritized images with the rest (randomized), ensuring no duplicates
  const remainingImages = allImages.filter(img => !prioritizedImages.includes(img));
  const shuffledRemainingImages = remainingImages.sort(() => Math.random() - 0.5);
  const images = [...prioritizedImages, ...shuffledRemainingImages];

  let slideshowInterval;
  let isSlideshowRunning = true;

  function showImage(index) {
    const imgElement = document.getElementById('slideshow-image');
    imgElement.src = images[index];

    // Adjust timing for .gif files
    const isGif = images[index].endsWith('.gif');
    const duration = isGif ? getGifDuration(imgElement) : 3500;

    if (isSlideshowRunning) {
      clearInterval(slideshowInterval);
      slideshowInterval = setTimeout(nextImage, duration);
    }
  }

  function getGifDuration(imgElement) {
    // Default to 5 seconds if duration cannot be determined
    return 3500;
  }

  function nextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    showImage(currentIndex);
  }

  function prevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    showImage(currentIndex);
  }

  function toggleSlideshow() {
    const stopButton = document.getElementById('toggle-slideshow-button');
    if (isSlideshowRunning) {
      clearTimeout(slideshowInterval);
      stopButton.textContent = "Start";
    } else {
      slideshowInterval = setTimeout(nextImage, 3500);
      stopButton.textContent = "Stopp";
    }
    isSlideshowRunning = !isSlideshowRunning;
  }

  // Start the slideshow initially
  slideshowInterval = setTimeout(nextImage, 14750);
</script>

<div style="text-align: center; margin-top: 30px;">
  <div style="margin-bottom: 10px;">
    <button onclick="prevImage()" style="background-color: #002445; color: #ffffff; border: none; padding: 10px 20px; margin-right: 5px; cursor: pointer; border-radius: 10px;">Forrige</button>
    <button id="toggle-slideshow-button" onclick="toggleSlideshow()" style="background-color: #8c8e95; color: #002445; border: 1px solid #8c8e95; padding: 10px 20px; margin: 0 5px; cursor: pointer; border-radius: 10px;">Stopp</button>
    <button onclick="nextImage()" style="background-color: #002445; color: #ffffff; border: none; padding: 10px 20px; margin-left: 5px; cursor: pointer; border-radius: 10px;">Neste</button>
  </div>
  <img id="slideshow-image" src="./assets/images/arkiv/500.gif" alt="Slideshow" style="width: 80%; height: auto; object-fit: contain; border: 2px solid #8c8e95; border-radius: 10px;" />
</div>
