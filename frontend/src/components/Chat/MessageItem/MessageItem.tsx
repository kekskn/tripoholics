import React from "react";
import cn from "classnames";

import Avatar from "../Avatar/Avatar";

import "./MessageItem.scss";

export default function MessageItem({ isMy, isOnline, isRead }) {
  return (
    <div className={cn("message-item", { my: isMy })}>
      <div className="message-item__avatar">
        <Avatar height={40} width={40} isOnline={isOnline} />
      </div>
      <div className={cn("message-item__text", { read: isRead })}>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae,
        suscipit perferendis dolor recusandae
      </div>
    </div>
  );
}
