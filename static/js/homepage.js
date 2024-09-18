document.addEventListener("DOMContentLoaded", function() {
    let count = 1;
    let intervalId;
    var radiosSlider = document.querySelectorAll("input[name='radio-btn-slider']");
    var carousels = document.querySelectorAll(".carousel");
    var rightButtonSlider = document.getElementById("rightButtonSlider");
    var leftButtonSlider = document.getElementById("leftButtonSlider");


    document.getElementById("radio1-slider").checked = true;
    document.getElementById("radio1-carousel1").checked = true;
    document.getElementById("radio1-carousel2").checked = true;
    document.getElementById("radio1-carousel3").checked = true;
    document.getElementById("radio1-carousel4").checked = true;
    document.getElementById("radio1-carousel5").checked = true;
    document.getElementById("radio1-carousel6").checked = true;
    startInterval();


    carousels.forEach(function(carousel, index) {
        index += 1
        var rightButtonCarousel = document.getElementById("rightButtonCarousel"+index)
        var leftButtonCarousel = document.getElementById("leftButtonCarousel"+index)
        var radiosCarousel = document.querySelectorAll(`input[name='radio-btn-carousel${index}']`)

        if (rightButtonCarousel) {
            rightButtonCarousel.addEventListener("click", function() {
                radiosCarousel.forEach(function(radio, i) {
                    if (radio.checked) {
                        count = 2 + i
    
                        if (radiosCarousel.length === 2) {
                            if (count > 2) {
                                count = 1
                            }
                        } else {
                            if (count > 3) {
                                count = 1
                            }
                        }
                    }
                })
    
                document.getElementById(`radio`+ count + "-carousel" + index).checked = true;
                startInterval(); 
            })
        }

        if (leftButtonCarousel) {
            leftButtonCarousel.addEventListener("click", function() {
                radiosCarousel.forEach(function(radio, i) {
                    if (radio.checked) {
                        count = 2 + i
    
                        if (radiosCarousel.length === 2) {
                            if (i === 0) {
                                count = 2
                            } else {
                                count = i
                            }
                        } else {
                            if (i === 0) {
                                count = 3
                            } else {
                                count = i
                            }
                        }
                    }
                })
    
                document.getElementById(`radio`+ count + "-carousel" + index).checked = true;
                startInterval(); 
            })
        }
    });


    rightButtonSlider.addEventListener("click", function() {
        nextImage();
    });

    leftButtonSlider.addEventListener("click", function() {
        radiosSlider.forEach(function(radio, index) {
            if (radio.checked) {
                if (index === 0) {
                    count = 4
                } else {
                    count = index
                }
            }
        })

        document.getElementById(`radio`+ count + "-slider").checked = true;
        startInterval(); 
    });


    function nextImage() {
        radiosSlider.forEach(function(radio, index) {
            if (radio.checked) {
                count = 2 + index

                if (count > 4) {
                    count = 1
                }
            }
        })

        document.getElementById(`radio`+ count + "-slider").checked = true;
        startInterval(); 
    }
    
    function startInterval() {
        if (intervalId) {
            clearInterval(intervalId);
        }

        intervalId = setInterval(function() {
            nextImage();
        }, 5000);
    }
})