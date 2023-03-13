import { createAction } from "@reduxjs/toolkit";
import {
  ON_LOAD,
  SEND_NEW_MESSAGE,
  GET_CURRENT_DIALOG,
  GET_CURRENT_EMPTY_DIALOG,
  CREATE_NEW_DIALOG,
} from "../constants";
import chatSlice from "../reducers/chat";
import userSlice from "../reducers/user";

export const { setUserInfo } = userSlice.actions;
export const {
  setDialogs,
  setCurrentDialog,
  fetchDialog,
  setMessages,
  addNewMessage,
  fetchNewDialog,
  openNewDialog,
  setRealDialogFromEmptyDialog,
} = chatSlice.actions;

export const onLoad = createAction(ON_LOAD);
export const sendNewMessage = createAction(SEND_NEW_MESSAGE);
export const getCurrentDialog = createAction(GET_CURRENT_DIALOG);
export const getCurrentEmptyDialog = createAction(GET_CURRENT_EMPTY_DIALOG);
export const createNewDialog = createAction(CREATE_NEW_DIALOG);
