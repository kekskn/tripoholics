import React from "react";
import cn from "classnames";

import "./Avatar.scss";

type Props = {
  height: number;
  width: number;
  isOnline: boolean;
};

export default function Avatar({ height, width, isOnline }: Props) {
  return (
    // <div className="dialog-item__avatar">
    <div className={cn("avatar", { online: isOnline })}>
      <img
        src="https://demiart.ru/forum/uploads17/post-608432-1462818506.jpg"
        alt="avatar"
        style={{
          height: `${height}px`,
          width: `${width}px`,
          borderRadius: "50%",
        }}
      />
    </div>
  );
}
