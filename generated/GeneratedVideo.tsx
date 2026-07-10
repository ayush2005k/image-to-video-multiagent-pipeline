import React from "react";
import {
    AbsoluteFill,
    Sequence,
    Img,
    useCurrentFrame,
    interpolate,
    staticFile,
} from "remotion";

// Component for the first scene content, including its specific logic
const Scene1Content: React.FC = () => {
    const frame = useCurrentFrame();
    const fadeDuration = 30; // 1 second fade-in

    // Opacity for fade-in effect
    const opacity = interpolate(
        frame,
        [0, fadeDuration],
        [0, 1],
        { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
    );

    return (
        <AbsoluteFill>
            <Img
                src={staticFile("GHZQ9770.JPG")}
                style={{
                    opacity,
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
                    opacity, // Apply fade to caption as well
                }}
            >
                Night's embrace.
            </div>
        </AbsoluteFill>
    );
};

export const GeneratedVideo: React.FC = () => {
    return (
        <AbsoluteFill style={{ backgroundColor: "black" }}>
            {/* Scene 1: Night's embrace. */}
            <Sequence from={0} durationInFrames={120}> {/* 4.0 seconds * 30 fps = 120 frames */}
                <Scene1Content />
            </Sequence>
        </AbsoluteFill>
    );
};
