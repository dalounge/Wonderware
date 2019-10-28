using System;
using System.Net.NetworkInformation;

namespace PingResults
{
    class Program
    {
        static void Main(string[] args)
        {
            Ping ping = new Ping();
            PingReply reply = ping.Send("google.com");
            Console.WriteLine($"Ping IP Address: {reply.Address}");
            Console.WriteLine($"Ping Status: {reply.Status}");
            Console.WriteLine($"Ping RoundTripTime: {reply.RoundtripTime}");
        }
    }
}
