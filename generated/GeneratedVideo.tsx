import React from "react";
import {
    AbsoluteFill,
    Sequence,
    Img,
    useCurrentFrame,
    interpolate,
    staticFile
} from "remotion";

export const GeneratedVideo: React.FC = () => {
    return (
        <AbsoluteFill style={{ backgroundColor: "black" }}>
            {/* Scene 1: Night's Embrace. */}
            <Sequence from={0} durationInFrames={120}>
                <Scene1 />
            </Sequence>
        </AbsoluteFill>
    );
};

const Scene1: React.FC = () => {
    const frame = useCurrentFrame();

    // Fade transition for the first 30 frames
    const opacity = interpolate(
        frame,
        [0, 30],
        [0, 1],
        {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
        }
    );

    return (
        <AbsoluteFill style={{ opacity }}>
            <Img
                src={staticFile("GHZQ9770.JPG")}
                style={{
                    width: "100%",
                    height: "100%",
                    objectFit: "cover",
                }}
            />
            <div
                style={{
                    position: "absolute",
                    bottom: 50,
                    width: "100%",
                    textAlign: "center",
                    color: "white",
                    fontSize: 60,
                    fontWeight: "bold",
                    textShadow: "2px 2px 4px rgba(0,0,0,0.7)",
                    fontFamily: "sans-serif", // Added for better readability
                }}
            >
                Night's Embrace.
            </div>
        </AbsoluteFill>
    );
};
