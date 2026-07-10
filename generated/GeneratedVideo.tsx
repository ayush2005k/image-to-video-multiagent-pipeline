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
    const frame = useCurrentFrame();

    // Scene 1: Night's glow.
    const scene1DurationInFrames = 4.0 * 30; // 120 frames
    const scene1StartFrame = 0.0 * 30; // 0 frames

    const scene1Opacity = interpolate(
        frame,
        [scene1StartFrame, scene1StartFrame + 30], // Fade in over 1 second (30 frames)
        [0, 1],
        {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
        }
    );

    return (
        <AbsoluteFill style={{ backgroundColor: "black" }}>
            {/* Scene 1: Night's glow. */}
            <Sequence from={scene1StartFrame} durationInFrames={scene1DurationInFrames}>
                <Img
                    src={staticFile("GHZQ9770.JPG")}
                    style={{
                        opacity: scene1Opacity,
                        width: "100%",
                        height: "100%",
                        objectFit: "cover",
                    }}
                />
                <div
                    style={{
                        fontFamily: "Arial, sans-serif",
                        fontSize: "50px",
                        fontWeight: "bold",
                        color: "white",
                        textAlign: "center",
                        position: "absolute",
                        width: "100%",
                        bottom: "10%",
                        opacity: scene1Opacity, // Apply fade to caption as well
                    }}
                >
                    Night's glow.
                </div>
            </Sequence>
        </AbsoluteFill>
    );
};
