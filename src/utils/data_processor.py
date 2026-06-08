"""
Data processing utilities

Various utility functions for data processing.
"""

from typing import List, Any
import json


class DataProcessor:
    """Process and transform data"""
    
    def __init__(self):
        self.cache = {}
    
    def process_batch(self, items: List[dict]) -> List[dict]:
        """
        Process a batch of items
        
        Args:
            items: List of items to process
            
        Returns:
            Processed items
        """
        results = []
        
        # PERFORMANCE ISSUE: Inefficient algorithm (O(n²))
        for item in items:
            for other_item in items:
                if item['id'] != other_item['id']:
                    if self._is_related(item, other_item):
                        item['related'] = item.get('related', [])
                        item['related'].append(other_item['id'])
            
            results.append(item)
        
        return results
    
    def _is_related(self, item1: dict, item2: dict) -> bool:
        """Check if two items are related"""
        # Simple check for demo purposes
        return item1.get('category') == item2.get('category')
    
    def transform_data(self, data: Any, format: str) -> str:
        """
        Transform data to specified format
        
        Args:
            data: Data to transform
            format: Output format
            
        Returns:
            Transformed data as string
        """
        # ARCHITECTURE ISSUE: Large if-else chain (should use strategy pattern)
        if format == 'json':
            return json.dumps(data)
        elif format == 'csv':
            return self._to_csv(data)
        elif format == 'xml':
            return self._to_xml(data)
        elif format == 'yaml':
            return self._to_yaml(data)
        elif format == 'text':
            return str(data)
        else:
            return str(data)
    
    def _to_csv(self, data: Any) -> str:
        """Convert to CSV"""
        # Simplified implementation
        return "csv_data"
    
    def _to_xml(self, data: Any) -> str:
        """Convert to XML"""
        # Simplified implementation
        return "<data></data>"
    
    def _to_yaml(self, data: Any) -> str:
        """Convert to YAML"""
        # Simplified implementation
        return "yaml_data"
    
    def merge_data(self, list1: List[dict], list2: List[dict]) -> List[dict]:
        """
        Merge two lists of dictionaries
        
        Args:
            list1: First list
            list2: Second list
            
        Returns:
            Merged list
        """
        # ARCHITECTURE ISSUE: Code duplication, should extract to method
        result = []
        
        for item1 in list1:
            found = False
            for item2 in list2:
                if item1.get('id') == item2.get('id'):
                    merged = {}
                    for key in item1:
                        merged[key] = item1[key]
                    for key in item2:
                        merged[key] = item2[key]
                    result.append(merged)
                    found = True
                    break
            
            if not found:
                result.append(item1)
        
        # Same logic repeated for list2
        for item2 in list2:
            found = False
            for item in result:
                if item.get('id') == item2.get('id'):
                    found = True
                    break
            
            if not found:
                result.append(item2)
        
        return result
