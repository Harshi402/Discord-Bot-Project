# Discord-Bot-Project
<p> <b>Idea: I had been using discord for long, and every time I encountered a bot message, I always got curious so I decided to implement a discord bot myself.  </b></p>
<p> The functions of this bot:
  <ol type="1">
    <li>Whenever a new user enters the server, the bot will welcome them displaying the message "Welcome to <ServerName>". </li>
      <li>Command "kick" to kick any user. This can be done by the server owner to kick a user out of the server. 
        A co-routine is called if somebody uses this command but they don't have the permission to do so.</li>
      <li>Command "ban" to ban a user from the server. This can also be only done by the owner of the server but if somebody else tries to do so, a co-routine will be called and the bot will display an error message "you don't have the permission."</li>
      <li>The bot will display a joke message when a new user enters the server. I had included this for them to have fun. This is done using a random joke Rapid API.</li>
      <li>When a user leaves the server, the bot displays the message "GoodBye <userid>".</li>
  </ol>
      </p>
