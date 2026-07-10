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
    // Scene 1
    // image: 'GHZQ9770.JPG'
    // start_time: 0.0
    // duration: 4.0
    // caption: 'Shared joy.'
    // transition: 'fade'

    // Convert duration to frames
    const scene1DurationFrames = 4.0 * 30; // 120 frames

    return (
        <AbsoluteFill style={{ backgroundColor: "black" }}>
            <Sequence from={0} durationInFrames={scene1DurationFrames}>
                <SceneContent
                    image="GHZQ9770.JPG"
                    caption="Shared joy."
                    transition="fade"
                    durationInFrames={scene1DurationFrames}
                />
            </Sequence>
        </AbsoluteFill>
    );
};

interface SceneContentProps {
    image: string;
    caption: string;
    transition: "fade" | "cut" | "zoom" | "slide" | "crossfade";
    durationInFrames: number;
}

const SceneContent: React.FC<SceneContentProps> = ({
    image,
    caption,
    transition,
    durationInFrames
}) => {
    const frame = useCurrentFrame();
    let style: React.CSSProperties = {};

    if (transition === "fade") {
        const opacity = interpolate(
            frame,
            [0, 30], // Fade in over 1 second (30 frames)
            [0, 1],
            { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
        );
        style = { opacity };
    }

    return (
        <AbsoluteFill style={style}>
            <Img
                src={staticFile(image)}
                style={{ width: "100%", height: "100%", objectFit: "cover" }}
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
                    textShadow: "2px 2px 4px rgba(0,0,0,0.7)"
                }}
            >
                {caption}
            </div>
        </AbsoluteFill>
    );
};