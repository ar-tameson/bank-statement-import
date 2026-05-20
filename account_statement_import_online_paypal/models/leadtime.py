aaa = env['product.supplierinfo'].search([
    ("partner_id", "=", 12),
    ("product_tmpl_id.active", "=", True),
    ("product_tmpl_id.bom_ids", "=", False),
])
bbb = aaa.filtered(lambda aa: not aa.default_code.startswith("TMP-") and not aa.default_code.startswith("LD"))

# Group by delay field
grouped_by_delay = {}
for record in bbb:
    delay = record.delay
    if delay not in grouped_by_delay:
        grouped_by_delay[delay] = []
    grouped_by_delay[delay].append(record.id)

# Update each group with delay + 1
for delay, record_ids in grouped_by_delay.items():
    env['product.supplierinfo'].browse(record_ids).write({'delay': delay + 1})
    