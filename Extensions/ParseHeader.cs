using Bonsai;
using System;
using System.Text;
using System.ComponentModel;
using System.Collections.Generic;
using System.Linq;
using System.Reactive.Linq;

[Combinator]
[Description("Parses the header information of a ZMQ message.")]
[WorkflowElementCategory(ElementCategory.Transform)]
public class ParseHeader
{
    public IObservable<string> Process(IObservable<byte[]> source)
    {
        return source.Select(value =>
        {
            string json = Encoding.UTF8.GetString(value);
            return json;
        });
    }
}
