using Bonsai;
using System;
using System.Text;
using System.ComponentModel;
using System.Collections.Generic;
using System.Linq;
using System.Reactive.Linq;

[Combinator]
[Description("Parses the data payload of a ZMQ message.")]
[WorkflowElementCategory(ElementCategory.Transform)]
public class ParseData
{
    public IObservable<int> Process(IObservable<byte[]> source)
    {
        return source.Select(value =>
        {
            var intVal = BitConverter.ToInt32(value, 0);
            return intVal;
        });
    }
}
