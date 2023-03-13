import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  id: null,
  name: undefined,
  surname: undefined,
};

const userSlice = createSlice({
  name: "user",
  initialState,
  reducers: {
    setUserInfo: (state, { payload }) => {
      state.id = payload.id;
      state.name = payload.first_name;
      state.surname = payload.last_name;
    },
  },
});

export default userSlice;
