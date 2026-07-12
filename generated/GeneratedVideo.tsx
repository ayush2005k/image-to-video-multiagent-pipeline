import React from "react";
import {
    AbsoluteFill,
    Sequence,
    Img,
    staticFile,
    // useCurrentFrame,
    // interpolate
} from "remotion";

export const GeneratedVideo: React.FC = () => {
    return (
        <AbsoluteFill style={{
            backgroundColor: "black"
        }}>
            {/* Scene 1: TRIUMPHANT ROAR! */}
            <Sequence from={0} durationInFrames={60}>
                <Img src={staticFile("goal1.jpg")}
                 style={{
                    width: "100%",
                    height: "100%",
                    objectFit: "cover"
                }} />
                <div style={{
                    position: "absolute",
                    bottom: 20,
                    width: "100%",
                    textAlign: "center",
                    color: "white",
                    fontSize: 50,
                    fontWeight: "bold",
                    textShadow: "2px 2px 4px rgba(0,0,0,0.7)"
                }}>
                    TRIUMPHANT ROAR!
                </div>
            </Sequence>

            {/* Scene 2: VICTORY'S SWEET CONTRAST! */}
            <Sequence from={60} durationInFrames={60}>
                <Img src={staticFile("goal2.jpg")} 
                style={{
                    width: "100%",
                    height: "100%",
                    objectFit: "cover"
                }} />
                <div style={{
                    position: "absolute",
                    bottom: 20,
                    width: "100%",
                    textAlign: "center",
                    color: "white",
                    fontSize: 50,
                    fontWeight: "bold",
                    textShadow: "2px 2px 4px rgba(0,0,0,0.7)"
                }}>
                    VICTORY'S SWEET CONTRAST!
                </div>
            </Sequence>

            {/* Scene 3: UNBRIDLED JOY! */}
            <Sequence from={120} durationInFrames={60}>
                <Img src={staticFile("goal3.jpg")}
                style={{
                    width: "100%",
                    height: "100%",
                    objectFit: "cover"
                }} />
                <div style={{
                    position: "absolute",
                    bottom: 20,
                    width: "100%",
                    textAlign: "center",
                    color: "white",
                    fontSize: 50,
                    fontWeight: "bold",
                    textShadow: "2px 2px 4px rgba(0,0,0,0.7)"
                }}>
                    UNBRIDLED JOY!
                </div>
            </Sequence>

            {/* Scene 4: CROWD ERUPTS! */}
            <Sequence from={180} durationInFrames={60}>
                <Img src={staticFile("goal4.jpg")}
                style={{
                    width: "100%",
                    height: "100%",
                    objectFit: "cover"
                }} />
                <div style={{
                    position: "absolute",
                    bottom: 20,
                    width: "100%",
                    textAlign: "center",
                    color: "white",
                    fontSize: 50,
                    fontWeight: "bold",
                    textShadow: "2px 2px 4px rgba(0,0,0,0.7)"
                }}>
                    CROWD ERUPTS!
                </div>
            </Sequence>
        </AbsoluteFill>
    );
};