// Declare a "SerialPort" object
var serial;
var latestData = "data"; 
var r,g,b
// you'll use this to write incoming data to the canvas

function setup() {
  createCanvas(500, 500);


  // STEP 1 Instantiate our SerialPort object
  serial = new p5.SerialPort();
	
  // STEP 2 Set port (Get this from p5 serial control app!)
  serial.open("/dev/cu.usbserial-DN051353");

  // STEP 3 set up a callback to read data
  serial.onData(gotData);

  noStroke();
}

// Data
function gotData() {
  // Step 4a: read the data
  var currentString = serial.readLine(); // read the incoming string
  if (!currentString) return; // if the string is empty, do no more
  latestData = Number(currentString); // save it for the draw method
}

function draw() {
  //r = random(255)
  //b = random(255)
  //g = random(255)
  
  if (latestData > 100 && latestData<300) {
		background ((map(latestData, 0, 1023, 100,255)),50,(map(latestData, 0, 1023, 200, 0)));}
  else if (latestData > 300) {
    background ((map(latestData, 0, 1023, 255,0)),(map(latestData, 0, 1023, 100, 0)),(100));}

    if (latestData > 100 && latestData<300) {
		text("circles");}
  
  // Step 4b: use the data
    text(latestData, 10, 10);
  
  var data1 = map(latestData, 0, 1023, 0, 500);
  var data2 = map(latestData, 0, 1023, 0, 200);
  var data3 = map(latestData, 0, 1023, 0, 300);
  var data4 = map(latestData, 0, 1023, 0, 200);
  var data5 = map(latestData, 0, 1023, 0, 200);


  	
  //middle circle
  fill(50,50+data1,data1);
  ellipse(250, 250, data1);
 
  
  //top left circle
  fill(0+data2,115,200,100);
  ellipse(80, 100, data2);
  
  //top right circle
  fill(115,data3,150,20);
  ellipse(350, 100, data3);

  //bottom right circle
  fill(255, 0+data4, 150,data4);
  ellipse(350, 400, data4);
  
  //bottom left circle
  ellipse(100, 380, data5);
    fill(data5,115,300,data5);

  
}