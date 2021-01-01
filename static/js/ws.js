const WS = new WebSocket("ws://localhost:8080/get_mileage_data")

WS.onopen = (event) => {
  console.log("WS connected");
};

WS.onmessage = (event) => {
  console.log("received: "+event.data);
};

WS.onclose = (event) => {
  console.log(`WS closed, code: ${event.code}, reason = ${event.reason}`)
};

WS.onerror = (error) => {
  console.log(error.message);
};
