import React, { useState } from "react";
import { formatDistance, parseISO } from "date-fns";
import ru from "date-fns/esm/locale/ru/index.js";

import Avatar from "../Avatar/Avatar";
import renderDialogItemMessage from "../../../utils/renderDialogItemMessage";

import "./DialogItem.scss";
import { NavLink } from "react-router-dom";
import { useSelector } from "react-redux";
import { RootState } from "src/redux/store";

export default function DialogItem({
  // date,
  companion,
  dialogId,
  isEmptyDialog,
  isOnline,
  lastMessage,
  avatar,
}) {
  const userId = useSelector((state: RootState) => state.user.id);
  const [isActiveDialog, setIsActiveDialog] = useState(false);
  let activeStyle = {
    textDecoration: "none",
  };
  let notActiveStyle = {
    textDecoration: "none",
    color: "inherit",
  };

  return (
    <NavLink
      to={`/my_messages/${isEmptyDialog ? `new_dialog/${dialogId}` : dialogId}`}
      className="dialog-item-link"
      style={({ isActive }) => {
        if (isActive) {
          setIsActiveDialog(true);
          return activeStyle;
        } else {
          setIsActiveDialog(false);
          return notActiveStyle;
        }
      }}
    >
      <div className="dialog-item">
        <div className="dialog-item__avatar">
          <Avatar
            height={48}
            width={48}
            isOnline={isOnline}
            letter={companion[0]}
            img={avatar}
          />
        </div>
        <div className="dialog-item__info-wrapper">
          <div className="dialog-item__info">
            <div className="dialog-item__fullname">{companion}</div>
            {lastMessage && (
              <div className="dialog-item__date">
                {formatDistance(parseISO(lastMessage.date), new Date(), {
                  addSuffix: true,
                  locale: ru,
                })}
              </div>
            )}
          </div>
          <div className="dialog-item__messages">
            {lastMessage && (
              <div className="dialog-item__last-message">
                {renderDialogItemMessage(
                  lastMessage.message_content,
                  lastMessage.author === userId
                )}
              </div>
            )}
            {!isActiveDialog && lastMessage && (
              <div className="dialog-item__unread-messages">3</div>
            )}
          </div>
        </div>
      </div>
    </NavLink>
  );
}
