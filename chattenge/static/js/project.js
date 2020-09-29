$(document).ready(() => {

  const chatrooms = (utils) => {
    /*
     * Perform a post request to send a message in the chatroom.
    **/
    const postMessageToChatroom = (chatroomUrl, content) => {
      return utils.post(chatroomUrl, { content });
    }

    /*
     * Perform a post request to include the user as a member in the chatroom.
    **/
    const joinChatroom = (chatroomUrl) => {
      return utils.post(chatroomUrl, {});
    }

    /*
     * Perform a post request to include the user as a member in the chatroom.
    **/
    const leaveChatroom = (chatroomUrl) => {
      return utils.post(chatroomUrl, {});
    }

    /*
     * Add a message to the message list
    **/
    const addMessage = (messageData) => {
      console.log(messageData);
    }

    return {
      postMessageToChatroom,
      joinChatroom,
      leaveChatroom,
      addMessage,
    };
  }

  const utils = () => {
    const DEFAULT_HEADERS = { 'Content-Type': 'application/json' }

    const post = async (url, body, headers) => {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          ...DEFAULT_HEADERS,
          ...headers
        },
        body: JSON.stringify(body),
      });
      return response ? response.json() : '';
    }

    const get = async (url, headers) => {
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          ...DEFAULT_HEADERS,
          ...headers
        }
      });
      return response ? response.json() : '';
    }
     
    return {
      post,
      get
    }
  }

  const _utils = utils();

  const exports = {
    utils: _utils,
    chatrooms: chatrooms(_utils),
  }

  window.chattenge = exports;
});
