// Model.js
import { useLoader } from "@react-three/fiber";
import { FBXLoader } from "three/examples/jsm/loaders/FBXLoader";

export default function Model(props) {
	const fbx = useLoader(FBXLoader, "/Connect4OG.fbx");
	const scaleValue = 0.2;
	fbx.scale.set(scaleValue, scaleValue, scaleValue);
	return (
		<>
			<primitive object={fbx} {...props} />
		</>
	);
}
