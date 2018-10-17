var xpos = 255;
var ypos = 25;
var xspeed = 2;
var yspeed = 2;
var xposrect;

function setup() {
  createCanvas(500, 500);
  fill(random(255),random(255),random(255));
  noStroke();
  rectMode(CENTER);
}

function draw() {
  background(0);
  ellipse(xpos, ypos, 30, 30); //ball

  
  
  //keep rectangle on screen

  if (mouseX >= 40 && mouseX <= width - 40) {
    xposrect = mouseX;
  } else if (mouseX < 40) {
    xposrect = 40;
  } else if (mouseX > width - 40) {
    xposrect = width - 40;
  }
  rect(xposrect, height - 2.5, 80, 30);

  //Making the ball move
  xpos += xspeed;
  ypos += yspeed;

  //Making the ball bounce out of left,top and right edges
  if (xpos <= 25 || xpos >= width - 25) {
    if (xspeed < 10 && xspeed > -10) { //speed
      xspeed = xspeed * (-1.2);
    } else {
      xspeed = xspeed * (-1.01);
    }
  }
  if (ypos <= 25) {
    if (yspeed < 10 && yspeed > -10) {
      yspeed = yspeed * (-1.2);
    } else {
      yspeed = yspeed * (-1.01);
    }
  }
  //ball bounce on rectangle
  if (ypos >= height - 25) {
    if (xpos <= xposrect + 65 && xpos >= xposrect - 65) {
      if (yspeed < 10 && yspeed > -10) {
        yspeed = yspeed * (-1.2);
      } else {
        yspeed = yspeed * (-1.01);
      }
    } else {
      textAlign(CENTER);
      textSize(40)
      textStyle(BOLD);
      text("GAME OVER", width / 2, height / 2);
      noLoop();
    }
  }
}

//random colors with mouse
function mousePressed() {
  fill(random(255), random(255), random(255));
}