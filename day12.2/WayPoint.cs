using System;
using System.Collections.Generic;
using System.Text;

namespace day122
{
    public class WayPoint
    {
        public int PosNorth { get; set; }
        public int PosEast { get; set; }

        public WayPoint(int north, int east)
        {
            PosNorth = north;
            PosEast = east;
        }

        internal void Move(char action, int value)
        {
            var direction = action.ToCardinal();

            if (direction == CardinalPoint.North || direction == CardinalPoint.South) PosNorth += value * direction.Sign();
            else PosEast += value * direction.Sign();
        }

        internal void Rotate(char action, int value)
        {
            var steps = value / 90;
            for (int i = 0; i < steps; i++)
            {
                if (action == 'L') RotateLeft();
                else RotateRight();
            }
        }

        private void RotateRight()
        {
            var oldNorthPos = PosNorth;
            var oldEastPos = PosEast;
            PosEast = oldNorthPos;
            PosNorth = -oldEastPos;

        }
        private void RotateLeft()
        {
            var oldNorthPos = PosNorth;
            var oldEastPos = PosEast;
            PosEast = -oldNorthPos;
            PosNorth = oldEastPos;
        }
    }
}
