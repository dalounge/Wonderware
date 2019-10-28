dim ping as System.Net.NetworkInformation.Ping;
dim reply as System.Net.NetworkInformation.PingReply;
ping = new System.Net.NetworkInformation.Ping;
reply = ping.Send("google.com");
LogMessage(reply.RoundtripTime);
RoundTripTime = reply.RoundtripTime;
