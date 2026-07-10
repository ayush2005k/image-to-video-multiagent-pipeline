import React from "react";
import {
    AbsoluteFill,
    Sequence,
    Img,
    useCurrentFrame,
    interpolate
} from "remotion";

export const GeneratedVideo: React.FC = () => {
    // Scene 1: Night's Embrace.
    const scene1DurationInFrames = 4 * 30; // 120 frames
    const scene1StartFrame = 0 * 30; // 0 frames

    return (
        <AbsoluteFill>
            <Sequence from={scene1StartFrame} durationInFrames={scene1DurationInFrames}>
                <Scene1Content />
            </Sequence>
        </AbsoluteFill>
    );
};

const Scene1Content: React.FC = () => {
    const frame = useCurrentFrame();

    // Fade-in over the first 30 frames of this sequence
    const opacity = interpolate(
        frame,
        [0, 30],
        [0, 1],
        { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
    );

    return (
        <>
            <Img src={"GHZQ9770.JPG"} style={{ opacity }} />
            <div
                style={{
                    position: "absolute",
                    bottom: 50,
                    width: "100%",
                    textAlign: "center",
                    color: "white",
                    fontSize: 50,
                    fontFamily: "sans-serif",
                    textShadow: "2px 2px 4px rgba(0,0,0,0.7)"
                }}
            >
                Night's Embrace.
            </div>
        </>
    );
};