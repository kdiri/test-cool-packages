import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

with beam.Pipeline(options=PipelineOptions()) as p:
    lines = p | 'Create' >> beam.Create(["cat dog", "snake cat", "dog"])
    counts = (
        lines
        | 'Split' >> beam.FlatMap(lambda x: x.split(" "))
        | 'PairWithOne' >> beam.Map(lambda x: (x, 1))
        | 'GroupAndSum' >> beam.CombinePerKey(sum)
    )
    counts | 'Print' >> beam.ParDo(lambda wc: print(f"{wc[0]} : {wc[1]}"))
