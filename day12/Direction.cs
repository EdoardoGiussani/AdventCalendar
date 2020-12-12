namespace day121
{
    public enum CardinalPoint
    {
        North,
        East,
        South,
        West
    }

    public static class CardinalExtensions
    {
        public static CardinalPoint Left(this CardinalPoint cardinalPoint)
        {
            var cardinalIndex = (int)cardinalPoint;
            cardinalIndex--;
            if (cardinalIndex < 0) cardinalIndex = 3;
            return (CardinalPoint)cardinalIndex;
        }
        public static CardinalPoint Right(this CardinalPoint cardinalPoint)
        {
            var cardinalIndex = (int)cardinalPoint;
            cardinalIndex++;
            if (cardinalIndex > 3) cardinalIndex = 0;
            return (CardinalPoint)cardinalIndex;
        }
        public static int Sign(this CardinalPoint cardinalPoint)
        {
            return cardinalPoint switch
            {
                CardinalPoint.North => 1,
                CardinalPoint.East => 1,
                CardinalPoint.South => -1,
                CardinalPoint.West => -1,
                _ => throw new System.NotImplementedException()
            };
        }

        public static CardinalPoint ToCardinal(this char action)
        {
            return action switch
            {
                'N' => CardinalPoint.North,
                'S' => CardinalPoint.South,
                'E' => CardinalPoint.East,
                'W' => CardinalPoint.West,
                _ => throw new System.NotImplementedException()
            };
        }
    }
}
