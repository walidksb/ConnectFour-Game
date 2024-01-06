import React from "react";
import "./Menu.css";

const Menu = () => {
	const quitClick = () => {
		// Redirect to the LandingPage page when the button is clicked
		window.location.href = "/";
	};
	const twoaiClick = () => {
		// Redirect to the game page with id 3 when the button is clicked
		window.location.href = "/game/3";
	};
	const oneaiClick = () => {
		// Redirect to the game page with id 2 when the button is clicked
		window.location.href = "/game/2";
	};
	const playersClick = () => {
		// Redirect to the game page with id 1 when the button is clicked
		window.location.href = "/game/1";
	};
	return (
		<div className="menu">
			<h1 className="menu-title">Menu</h1>
			<div className="buttons">
				<button className="menu-button" onClick={playersClick}>
					Player VS Player
				</button>
				<button className="menu-button" onClick={oneaiClick}>
					Player VS AI
				</button>
				<button className="menu-button" onClick={twoaiClick}>
					AI VS AI
				</button>
				<button className="menu-button" onClick={quitClick}>
					Quit
				</button>
			</div>
		</div>
	);
};

export default Menu;
