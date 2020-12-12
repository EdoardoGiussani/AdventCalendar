using System;
using System.Collections.Generic;
using System.Text;

namespace day121
{
    public class Ferry
    {
        public int PosNorth { get; set; } = 0;
        public int PosEast { get; set; } = 0;
        public CardinalPoint Facing { get; set; } = CardinalPoint.East;

        public void ExecuteInstruction(string instruction)
        {
            var action = instruction[0];
            var value = Convert.ToInt32(instruction[1..]);

            if (action == 'L' || action == 'R') Rotate(action, value);
            else Move(action, value);
        }

        private void Move(char action, int value)
        {
            CardinalPoint direction;
            if (action == 'F') direction = Facing;
            else direction = action.ToCardinal();

            if (direction == CardinalPoint.North || direction == CardinalPoint.South) PosNorth += value * direction.Sign();
            else PosEast += value * direction.Sign();
        }

        private void Rotate(char action, int value)
        {
            var steps = value / 90;
            for (int i = 0; i < steps; i++)
            {
                if (action == 'L') Facing = Facing.Left();
                else Facing = Facing.Right();
            }
        }
    }
}
