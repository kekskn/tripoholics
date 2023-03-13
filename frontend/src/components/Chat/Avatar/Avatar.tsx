import React from "react";
import cn from "classnames";

import letterToNumber from "./helpers/letterToNumber";
// import avatar from "../../../../static/photos/avatar.jpg";
import "./Avatar.scss";

type Props = {
  height: number;
  width: number;
  isOnline: boolean;
  letter: string;
  isSquare?: boolean;
};

export default function Avatar({
  height,
  width,
  isOnline,
  letter,
  isSquare,
}: Props) {
  return (
    <div
      className={cn("avatar", { online: isOnline })}
      style={{
        height: `${height}px`,
        width: `${width}px`,
        backgroundColor: `hsl(${letterToNumber[letter]}, 60%, 25%)`,
        borderRadius: `${isSquare ? "0" : "50%"}`,
      }}
    >
      {letter}
    </div>
  );
}
