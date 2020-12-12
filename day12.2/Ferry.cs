using System;
using System.Collections.Generic;
using System.Text;

namespace day122
{
    public class Ferry
    {
        public int PosNorth { get; set; } = 0;
        public int PosEast { get; set; } = 0;
        public WayPoint WayPoint { get; set; } = new WayPoint(1, 10);

        public void ExecuteInstruction(string instruction)
        {
            var action = instruction[0];
            var value = Convert.ToInt32(instruction[1..]);

            if (action == 'L' || action == 'R') WayPoint.Rotate(action, value);
            else if (action == 'F') Move(action, value);
            else WayPoint.Move(action, value);
        }

        private void Move(char action, int value)
        {
            PosNorth += WayPoint.PosNorth * value;
            PosEast += WayPoint.PosEast * value;
        }
    }
}
