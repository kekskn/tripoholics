import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  dialogs: [],
  currentDialog: {
    companion: undefined,
    companion_id: null,
    dialogId: undefined,
    is_online: false,
    isLoading: false,
    last_online_at: null,
    messages: undefined,
  },
  isCreatingNewDialog: false,
};

const chatSlice = createSlice({
  name: "chat",
  initialState,
  reducers: {
    setDialogs: (state, { payload }) => {
      state.dialogs = payload;
    },
    setCurrentDialog: (state, { payload }) => {
      state.currentDialog = {
        ...state.currentDialog,
        companion: payload.companion,
        companion_id: payload.companion_id,
        dialogId: payload.dialogId,
        is_online: payload.is_online,
        last_online_at: payload.last_online_at,
        messages: undefined,
      };
    },
    fetchDialog: (state) => {
      state.currentDialog = {
        ...state.currentDialog,
        messages: undefined,
        isLoading: true,
      };
    },
    setMessages: (state, { payload }) => {
      state.currentDialog = {
        ...state.currentDialog,
        messages: payload,
        isLoading: false,
      };
    },
    addNewMessage: (state, { payload }) => {
      state.currentDialog.messages = [...state.currentDialog.messages, payload];
    },
    fetchNewDialog: (state) => {
      state.isCreatingNewDialog = true;
    },
    openNewDialog: (state) => {
      state.isCreatingNewDialog = false;
    },
    setRealDialogFromEmptyDialog: (state, { payload }) => {
      // state.currentDialog = false;
      console.log("setRealDialogFromEmptyDialog", payload);

      const dialogs = [...state.dialogs];
      const dialog = dialogs.find((d) => d.dialog_id === payload.old_dialog_id);
      console.log("dialog from action", dialog);
      dialog.dialog_id = payload.new_dialog_id;
      dialog.isEmptyDialog = undefined;

      state.dialogs = dialogs;
    },
    changeDialogInterlocutorStatus: (state, { payload }) => {
      const dialogs = [...state.dialogs];
      const dialog = dialogs.find((d) => d.interlocutor_id === payload.user_id);
      console.log("dialog.is_ONLINE", dialog);
      dialog.is_online = payload.is_online;

      if (state.currentDialog.companion_id === payload.user_id)
        state.currentDialog.is_online = payload.is_online;

      state.dialogs = dialogs;
    },
  },
});

export default chatSlice;
