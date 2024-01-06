import { io } from "socket.io-client";

const socket = io("http://127.0.0.1:5000"); // Replace with your server URL

export default socket;
