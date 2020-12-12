﻿using System;
using System.IO;

namespace day122
{
    class Program
    {
        static void Main(string[] args)
        {
            var instructions = File.ReadAllLines(@"entries.txt");
            var ferry = new Ferry();
            foreach (var instruction in instructions)
            {
                ferry.ExecuteInstruction(instruction);
            }
            Console.WriteLine($"North: {ferry.PosNorth}, East: {ferry.PosEast}, Sum: {Math.Abs(ferry.PosNorth) + Math.Abs(ferry.PosEast)}");
        }
    }
}
