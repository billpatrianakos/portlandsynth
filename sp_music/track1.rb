live_loop :foo do
  use_real_time
  a, b, c = sync "/osc/trigger/prophet"
  synth :prophet, note: a, cutoff: b, sustain: c
end