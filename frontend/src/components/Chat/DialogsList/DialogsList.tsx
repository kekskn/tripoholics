import React, { useEffect } from "react";
import { useSelector } from "react-redux";
import { RootState } from "../../../redux/store";
import DialogItem from "../DialogItem/DialogItem";
import DialogsSearch from "../DialogsSearch/DialogsSearch";
import { Oval } from "react-loader-spinner";
import ContentLoader from "react-content-loader";
import "./DialogsList.scss";
import renderSkeleton from "./helpers/renderSkeleton";

export default function DialogsList() {
  const user = useSelector((store: RootState) => store?.user);
  const dialogs = useSelector((store: RootState) => store?.chat?.dialogs);
  useEffect(() => {
    console.log("dialogssssss: ", dialogs, user);
  }, [dialogs, user]);
  return (
    <div className="chat__dialogs-list">
      <DialogsSearch />
      <div className="chat__dialogs-list-wrapper">
        {dialogs.length
          ? dialogs.map((dialog) => {
              // let companion;
              // if (dialog.first_user_fio === `${user.name} ${user.surname}`) {
              //   companion = dialog.second_user_fio;
              // } else {
              //   companion = dialog.first_user_fio;
              // }
              return (
                <DialogItem
                  key={dialog.dialog_id}
                  date={new Date(Date.now() - 500000)}
                  companion={dialog.interlocutor}
                  roomName={dialog.dialog_id}
                  dialogId={dialog.dialog_id}
                />
              );
            })
          : renderSkeleton()}
      </div>
    </div>
  );
}
