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

    // Scene 1: Night's embrace. (fade transition)
    const scene1StartTime = 0 * 30; // 0 frames
    const scene1DurationFrames = 4 * 30; // 120 frames

    const opacity = interpolate(
        frame,
        [scene1StartTime, scene1StartTime + 30], // Fade in over the first 30 frames of the sequence
        [0, 1],
        {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
        }
    );

    return (
        <AbsoluteFill style={{ backgroundColor: "black" }}>
            <Sequence from={scene1StartTime} durationInFrames={scene1DurationFrames}>
                <Img src={staticFile("GHZQ9770.JPG")} style={{ opacity, width: "100%", height: "100%", objectFit: "cover" }} />
                <div
                    style={{
                        fontFamily: "sans-serif",
                        fontSize: 50,
                        textAlign: "center",
                        position: "absolute",
                        bottom: 50,
                        width: "100%",
                        color: "white",
                        opacity: opacity, // Apply fade to caption as well
                    }}
                >
                    Night's embrace.
                </div>
            </Sequence>
        </AbsoluteFill>
    );
};