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
  const images = [
    "./assets/images/arkiv/1.jpg",
    "./assets/images/arkiv/2.jpg",
    "./assets/images/arkiv/3.jpg",
    "./assets/images/arkiv/4.jpg",
    "./assets/images/arkiv/5.jpg"
    // Add more image paths as needed
  ];

  let slideshowInterval = setInterval(nextImage, 3000); // Change image every 3 seconds
  let isSlideshowRunning = true;

  function showImage(index) {
    const imgElement = document.getElementById('slideshow-image');
    imgElement.src = images[index];
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
      clearInterval(slideshowInterval);
      stopButton.textContent = "Start";
    } else {
      slideshowInterval = setInterval(nextImage, 3000);
      stopButton.textContent = "Stopp";
    }
    isSlideshowRunning = !isSlideshowRunning;
  }
</script>

<div style="text-align: center; margin-top: 30px;">
  <div style="margin-bottom: 10px;">
    <button onclick="prevImage()" style="background-color: #002445; color: #ffffff; border: none; padding: 10px 20px; margin-right: 5px; cursor: pointer; border-radius: 10px;">Forrige</button>
    <button id="toggle-slideshow-button" onclick="toggleSlideshow()" style="background-color: #8c8e95; color: #002445; border: 1px solid #8c8e95; padding: 10px 20px; margin: 0 5px; cursor: pointer; border-radius: 10px;">Stopp</button>
    <button onclick="nextImage()" style="background-color: #002445; color: #ffffff; border: none; padding: 10px 20px; margin-left: 5px; cursor: pointer; border-radius: 10px;">Neste</button>
  </div>
  <img id="slideshow-image" src="./assets/images/arkiv/1.jpg" alt="Slideshow" style="max-width: 80%; height: auto; object-fit: contain; border: 2px solid #8c8e95; border-radius: 10px;" />
</div>
