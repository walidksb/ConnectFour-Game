import React from "react";
import { useNavigate } from "react-router-dom";
import "./LandingPage.css";
import Envirement from "../Model/Envirement";

const LandingPage = () => {
	const navigate = useNavigate();

	const triggerPreview = () => {
		// Redirect to the Game page when the button is clicked
		navigate("/menu");
	};

	return (
		<div className="landingpage">
			<Envirement />
			<div className="container">
				<h1 className="title">Welcome To Connect Four Game</h1>
				<span className="description">
					A game designed using the most recent technologies of AI!
				</span>
				<button className="button" onClick={triggerPreview}>
					Play now!
				</button>
			</div>
		</div>
	);
};

export default LandingPage;
