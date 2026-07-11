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
            {/* Scene: Joyful journey. */}
            <Sequence from={0} durationInFrames={120}>
                <Scene1Content />
            </Sequence>
        </AbsoluteFill>
    );
};

const Scene1Content: React.FC = () => {
    const frame = useCurrentFrame();

    // Fade transition for the scene
    const opacity = interpolate(
        frame,
        [0, 30], // Fade in over the first 30 frames (1 second)
        [0, 1],
        { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
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
                    fontSize: 50,
                    fontWeight: "bold",
                    textShadow: "2px 2px 4px rgba(0,0,0,0.7)",
                    fontFamily: "sans-serif",
                }}
            >
                Joyful journey.
            </div>
        </AbsoluteFill>
    );
};
