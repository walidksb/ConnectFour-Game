import React from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./components/LandingPage/LandingPage";
import Game from "./components/Game/Game";
import Menu from "./components/Game/Menu";
import Rules from "./components/Rules/Rules";

export default function App() {
	return (
		<div className="App">
			<BrowserRouter>
				<Routes>
					<Route path="/" element={<LandingPage />} />
					<Route path="/game/:id" element={<Game />} />
					<Route path="/menu" element={<Menu />} />
					<Route path="/rules" element={<Rules />} />
				</Routes>
			</BrowserRouter>
		</div>
	);
}
